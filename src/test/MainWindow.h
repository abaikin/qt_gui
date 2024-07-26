#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPointer>

#include "ui_MainWindow.h"

class QTreeWidgetItem;

namespace scifrac {

class Notification;
class ProjectInfoPage;
class ProjectData;
class ProjectStackedWidget;
class ProjectView;

class MainWindow : public QMainWindow, private Ui_MainWindow {
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);

    void addNotification(const QString &message);

private slots:
    void sl_openStartPage();
    void sl_createNewProject();
    void sl_openProject();
    void sl_saveProject();
    void sl_saveProjectAs();
    void sl_closeProject();
    void sl_setStackedWidgetState(QTreeWidgetItem *);
    void sl_notificationHidden(Notification *);

private:
    void enableProjectRelatedButtons(const bool enable);
    void openProject(ProjectData *proj);
    void changeProject(ProjectData *newProj);
    bool saveChangedProjectAndContinue();
    void connectToFileAndSave();
    QPoint getBottomRightOfMainWindow();

    ProjectView *projectView;
    QWidget *startPage;
    QPointer<ProjectStackedWidget> stackedWidget;

    QList<Notification *> notifications;

    static const char *PROJECT_FILTER;
};

}    // namespace scifrac

#endif    // MAINWINDOW_H
