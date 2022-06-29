#ifndef EDITOR_HH
#define EDITOR_HH

#include <memory>
#include <string>

#include "EventManager.hh"
#include "File.hh"

using std::string;

class Editor {
public:
  std::unique_ptr<EventManager> events;
  Editor();
  ~Editor();
  void openFile(string filePath);
  void saveFile();

private:
  std::shared_ptr<File> _file;
};

#endif // EDITOR_HH
