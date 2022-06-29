#include <algorithm>
#include <iostream>
#include "EventManager.hh"

EventManager::EventManager() { }

EventManager::~EventManager() { }

bool EventManager::isValidOperation(string operation)
{
  return _listeners.find(operation) != _listeners.end();
}

void EventManager::addOperation(string operation)
{
  _listeners[operation] = vector<EventListenerPtr>();
}

void EventManager::subscribe(string eventType, EventListenerPtr listener)
{
  if (!isValidOperation(eventType)) {
    return;
  }
  _listeners[eventType].push_back(listener);
}

void EventManager::unsubscribe(string eventType, EventListenerPtr listener)
{
  if (!isValidOperation(eventType)) {
    return;
  }
  _listeners[eventType].erase(
    std::remove(
      _listeners[eventType].begin(),
      _listeners[eventType].end(),
      listener
    ),
    _listeners[eventType].end()
  );
}

void EventManager::notify(string eventType, FilePtr file)
{
  if (!isValidOperation(eventType)) {
    return;
  }
  for (auto& listener: _listeners[eventType]) {
    listener->update(eventType, file);
  }
}
