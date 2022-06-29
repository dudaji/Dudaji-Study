#include <string>
#include <memory>

#include "Editor.hh"
#include "File.hh"

using std::string;

Editor::Editor()
{
  events = std::make_unique<EventManager>();
  events->addOperation("open");
  events->addOperation("save");
  _file = nullptr;
}

Editor::~Editor() { }

void Editor::openFile(string filePath)
{
  _file = std::make_shared<File>(filePath);
  events->notify("open", _file);
}

void Editor::saveFile()
{
  if (_file != nullptr) {
    events->notify("save", _file);
  }
}
