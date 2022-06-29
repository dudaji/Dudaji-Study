#include "File.hh"

File::File(string filePath)
{
  _filePath = filePath;
}

File::~File() { }

string File::getName()
{
  return _filePath;
}
