#ifndef EVENT_MANAGER_HH
#define EVENT_MANAGER_HH

#include <string>
#include <map>
#include <vector>
#include <memory>

#include "EventListener.hh"
#include "File.hh"

using std::string;
using std::map;
using std::vector;
using EventListenerPtr = std::shared_ptr<EventListener>;
using FilePtr = std::shared_ptr<File>;

class EventManager {
public:
  EventManager();
  ~EventManager();
  bool isValidOperation(string operation);
  void addOperation(string operation);
  void subscribe(string eventType, EventListenerPtr listener);
  void unsubscribe(string eventType, EventListenerPtr listener);
  void notify(string eventType, FilePtr file);
private:
  map<string, vector<EventListenerPtr>> _listeners;
};

#endif // EVENT_MANAGER_HH
