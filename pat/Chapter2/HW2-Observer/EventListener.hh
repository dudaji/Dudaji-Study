#ifndef EVENT_LISTENER_HH
#define EVENT_LISTENER_HH

#include <string>
#include <memory>

#include "File.hh"

using std::string;
using FilePtr = std::shared_ptr<File>;

class EventListener {
public:
  virtual void update(string eventType, FilePtr file) = 0;
};

#endif // EVENT_LISTENER_HH
