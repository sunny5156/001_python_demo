#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>
#include <fstream>
#include <string>
 
using namespace cv;
using namespace std;

void Doreplace(string &str, const string &scr, const string &dst)
{
	while(1)
	{
		int pos = str.find(scr);
		if(pos<0) break;
		str.replace(pos,scr.length(),dst);
	}
}
 
 static inline std::string& ltrim(std::string& str, const std::string& chars = "\t\n\v\f\r ")
{
    str.erase(0, str.find_first_not_of(chars));
    return str;
}
 
static inline std::string& rtrim(std::string& str, const std::string& chars = "\t\n\v\f\r ")
{
    str.erase(str.find_last_not_of(chars) + 1);
    return str;
}
static inline std::string& trim(std::string& str, const std::string& chars = "\t\n\v\f\r ")
{
    return ltrim(rtrim(str, chars), chars);
}

int main() 
{
	filename "sdfewerwe\n";

	cout<<":::"<<  trim(filename);		
		// cout<<"--= "<<endl;		
}