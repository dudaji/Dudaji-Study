#ifndef LOGGING_LISTENER_HH
#define LOGGING_LISTENER_HH

#include <string>
#include <memory>

#include "EventListener.hh"
#include "File.hh"

using std::string;
using FilePtr = std::shared_ptr<File>;

class LoggingListener: public EventListener {
public:
  LoggingListener(string filePath);
  ~LoggingListener();
  void update(string eventType, FilePtr file);

private:
  std::unique_ptr<File> _log;
};

#endif // LOGGING_LISTENER_HH
