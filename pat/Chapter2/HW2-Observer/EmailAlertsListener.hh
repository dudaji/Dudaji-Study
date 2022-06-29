#ifndef EMAIL_ALERTS_LISTENER_HH
#define EMAIL_ALERTS_LISTENER_HH

#include <string>
#include <memory>

#include "EventListener.hh"
#include "File.hh"

using std::string;
using FilePtr = std::shared_ptr<File>;

class EmailAlertsListener: public EventListener {
public:
  EmailAlertsListener(string email);
  ~EmailAlertsListener();
  void update(string eventType, FilePtr file);
private:
  string _email;
};

#endif // EMAIL_ALERTS_LISTENER_HH
