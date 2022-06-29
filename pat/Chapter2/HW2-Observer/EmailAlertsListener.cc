#include <string>
#include <iostream>
#include <memory>

#include "EmailAlertsListener.hh"
#include "File.hh"

using std::string;
using std::cout;
using FilePtr = std::shared_ptr<File>;

EmailAlertsListener::EmailAlertsListener(string email)
{
  _email = email;
}

EmailAlertsListener::~EmailAlertsListener() { }

void EmailAlertsListener::update(string eventType, FilePtr file)
{
  cout << _email << ": " << eventType << " on " << file->getName() << '\n';
}
