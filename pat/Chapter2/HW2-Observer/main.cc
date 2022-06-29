#include <iostream>
#include <memory>

#include "Editor.hh"
#include "LoggingListener.hh"
#include "EmailAlertsListener.hh"

int main() {
  Editor editor;
  editor.events->subscribe("open",
    std::make_shared<LoggingListener>("/home/pat/editor.log"));
  editor.events->subscribe("save",
    std::make_shared<EmailAlertsListener>("pat@mymail.com"));

  editor.openFile("test.txt");
  editor.saveFile();
}
