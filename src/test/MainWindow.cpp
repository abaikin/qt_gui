#include "MainWindow.h"

#include <QDate>
#include <QDebug>
#include <QDockWidget>
#include <QFileDialog>
#include <QInputDialog>
#include <QLabel>
#include <QMessageBox>
#include <QSplitter>
#include <QTreeWidgetItem>
#include <QVBoxLayout>

#include "MenuBar.h"
#include "Notification.h"
#include "ProjectStackedWidget.h"
#include "ProjectView.h"
#include "backend/MessageException.h"
#include "backend/dictionaries/Dictionaries.h"
#include "backend/project/ProjectData.h"
#include "backend/project/ProjectJson.h"
#include "project_pages/ProjectInfoPage.h"

namespace scifrac {

const char *MainWindow::PROJECT_FILTER = QT_TR_NOOP("Project files (*.json *.scfrac *.scfracj)");

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent) {
    setupUi(this);

    auto mBar = new MenuBar(this);
    setMenuBar(mBar);
    connect(mBar->getStartPageAction(), SIGNAL(triggered(bool)), this, SLOT(sl_openStartPage()));
    connect(mBar->getCreateNewProjectAction(), SIGNAL(triggered(bool)), this, SLOT(sl_createNewProject()));
    connect(createNewProjectButton, SIGNAL(clicked()), this, SLOT(sl_createNewProject()));
    connect(mBar->getOpenProjectAction(), SIGNAL(triggered(bool)), this, SLOT(sl_openProject()));
    connect(openProjectButton, SIGNAL(clicked()), this, SLOT(sl_openProject()));
    connect(mBar->getSaveProjectAction(), SIGNAL(triggered(bool)), this, SLOT(sl_saveProject()));
    connect(mBar->getSaveProjectAsAction(), SIGNAL(triggered(bool)), this, SLOT(sl_saveProjectAs()));
    connect(mBar->getCloseProjectAction(), SIGNAL(triggered(bool)), this, SLOT(sl_closeProject()));

    enableProjectRelatedButtons(false);

    QDockWidget *dock = new QDockWidget(tr("Project View"), this);
    dock->setAllowedAreas(Qt::LeftDockWidgetArea);
    dock->setFeatures(QDockWidget::NoDockWidgetFeatures);
    projectView = new ProjectView(dock);
    dock->setWidget(projectView);
    addDockWidget(Qt::LeftDockWidgetArea, dock);
    connect(projectView->getTreeWidget(), SIGNAL(itemClicked(QTreeWidgetItem *, int)), this, SLOT(sl_setStackedWidgetState(QTreeWidgetItem *)));

    startPage = centralWidget();
}

void MainWindow::addNotification(const QString &message) {
    auto n = new Notification(message, this);
    int globalNotificationsHeight = 0;
    for (Notification *notification : notifications) {
        globalNotificationsHeight += notification->height();
    }
    QPoint bottomRight = getBottomRightOfMainWindow();
    bottomRight.setY(bottomRight.y() - globalNotificationsHeight);
    n->show(bottomRight);
    notifications << n;
    connect(n, SIGNAL(si_hidden(Notification *)), this, SLOT(sl_notificationHidden(Notification *)));
}

void MainWindow::sl_openStartPage() {
    auto centralWgt = centralWidget();
    if (startPage == centralWgt) {
        return;
    }

    Q_ASSERT(!stackedWidget.isNull());
    Q_ASSERT(stackedWidget == centralWgt);

    centralWgt->setParent(nullptr);
    setCentralWidget(startPage);
    stackedWidget->setParent(this);
}

void MainWindow::sl_createNewProject() {
    if (!saveChangedProjectAndContinue()) {
        return;
    }

    bool ok = false;
    QString projectName = tr("New project");
    QString projName = QInputDialog::getText(this, tr("Create new project"), tr("Project name"), QLineEdit::Normal, projectName, &ok);
    if (!ok) {
        return;
    }

    if (projectView->isProjectOpened()) {
        changeProject(new ProjectData(projName));
    } else {
        openProject(new ProjectData(projName));
    }
}

void MainWindow::sl_openProject() {
    QString fileName = QFileDialog::getOpenFileName(this, tr("Open project"), QString(), tr(PROJECT_FILTER));
    if (fileName.isEmpty()) {
        return;
    }

    ProjectData *proj = nullptr;
    try {
        QFile prjFile(fileName);
        QFileInfo fi(fileName);
        if (fi.suffix() == "json") {
            Dictionaries::getInstance()->appendFromJsonAndSave(fileName);
            proj = ProjectJson::load(fileName);
        } else {
            proj = new ProjectData(prjFile);
            proj->setFile(fileName);
        }
    } catch (const MessageException &ex) {
        addNotification(ex.getMessage());
        return;
    }
    Q_ASSERT(proj != nullptr);

    if (projectView->isProjectOpened()) {
        changeProject(proj);
    } else {
        openProject(proj);
    }
}

void MainWindow::sl_saveProject() {
    if (projectView->isProjectConnectedToFile()) {
        projectView->saveProject();
    } else {
        connectToFileAndSave();
    }
}

void MainWindow::sl_saveProjectAs() {
    connectToFileAndSave();
}

void MainWindow::sl_closeProject() {
    Q_ASSERT(projectView->isProjectOpened());

    projectView->closeProject();

    auto centralWgt = centralWidget();
    if (centralWgt == startPage) {
        stackedWidget->deleteLater();
    } else if (centralWgt == stackedWidget) {
        setCentralWidget(startPage);
    } else {
        Q_ASSERT(false);
    }

    enableProjectRelatedButtons(false);
}

void MainWindow::sl_setStackedWidgetState(QTreeWidgetItem *item) {
    Q_ASSERT(stackedWidget != nullptr);

    if (centralWidget() == startPage) {
        startPage->setParent(nullptr);
        setCentralWidget(stackedWidget);
        startPage->setParent(this);
    }
    const QString className(item->data(0, Qt::UserRole).toString());
    if (!className.isEmpty()) {
        stackedWidget->switchCurrentWidget(className);
    }
}

void MainWindow::sl_notificationHidden(Notification *n) {
    Q_ASSERT(notifications.contains(n));

    const int index = notifications.indexOf(n);
    for (int i = notifications.size() - 1; i > index; i--) {
        notifications[i]->moveDown();
    }
    notifications.removeOne(n);
    n->deleteLater();
}

void MainWindow::enableProjectRelatedButtons(const bool enable) {
    auto mBar = qobject_cast<MenuBar *>(menuBar());
    Q_ASSERT(mBar != nullptr);

    mBar->getSaveProjectAction()->setEnabled(enable);
    mBar->getSaveProjectAsAction()->setEnabled(enable);
    mBar->getCloseProjectAction()->setEnabled(enable);
}

void MainWindow::openProject(ProjectData *proj) {
    Q_ASSERT(!projectView->isProjectOpened());

    startPage->setParent(nullptr);
    stackedWidget = new ProjectStackedWidget(proj, this);
    setCentralWidget(stackedWidget);
    startPage->setParent(this);

    projectView->setProject(proj);
    enableProjectRelatedButtons(true);
}

void MainWindow::changeProject(ProjectData *newProj) {
    Q_ASSERT(projectView->isProjectOpened());

    if (centralWidget() == startPage) {
        startPage->setParent(nullptr);
    }
    stackedWidget = new ProjectStackedWidget(newProj, this);
    setCentralWidget(stackedWidget);
    startPage->setParent(this);

    projectView->closeProject();
    projectView->setProject(newProj);
}

bool MainWindow::saveChangedProjectAndContinue() {
    bool continueExecution = true;
    if (projectView->isProjectChanged()) {
        auto reply = QMessageBox::question(this, tr("Save project?"), tr("The current opened project was changed, save before close?"), QMessageBox::Yes | QMessageBox::No | QMessageBox::Cancel);
        switch (reply) {
        case QMessageBox::Yes:
            sl_saveProject();
            [[fallthrough]];
        case QMessageBox::No:
            sl_closeProject();
            break;
        case QMessageBox::Cancel:
            continueExecution = false;
            break;
        default:
            Q_ASSERT(false);
        }
    }

    return continueExecution;
}

void MainWindow::connectToFileAndSave() {
    QString defaultFilePath = QCoreApplication::applicationDirPath() + "/" + projectView->getProjectName() + ".scfracj";
    QString saveFilePath = QFileDialog::getSaveFileName(this, tr("Save project"), defaultFilePath, tr(PROJECT_FILTER));
    if (saveFilePath.isEmpty()) {
        return;
    }

    projectView->saveProject(saveFilePath);
}

QPoint MainWindow::getBottomRightOfMainWindow() {
    QPoint pos;
#ifndef Q_OS_MAC
    // This behavior is correct.
    pos = geometry().bottomRight();
#else
    // Widget's rect doesn't know its real position on the screen. Lets calculate it manually.
    QPoint topLeft = mapToGlobal(QPoint(0, 0));
    QSize mainWindowSize = geometry().size();
    pos = QPoint(topLeft.x() + mainWindowSize.width(), topLeft.y() + mainWindowSize.height());    // bottom right
    pos -= QPoint(4, 27);    // Some space for the statusbar and window's edge.
#endif
    return pos;
}

}    // namespace scifrac
