#include <string>
#include <memory>
#include <iostream>

#include "LoggingListener.hh"
#include "File.hh"

using std::string;
using std::cout;
using FilePtr = std::shared_ptr<File>;

LoggingListener::LoggingListener(string filePath)
{
  _log = std::make_unique<File>(filePath);
}

LoggingListener::~LoggingListener() { }

void LoggingListener::update(string eventType, FilePtr file)
{
  cout << _log->getName() << ": " << eventType << " on " << file->getName() << '\n';
}
