#ifndef FILE_HH
#define FILE_HH

#include <string>

using std::string;

class File {
public:
  File(string filePath);
  ~File();
  string getName();

private:
  string _filePath;
};

#endif // FILE_HH
