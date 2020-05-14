#include <iostream>
#include "picojson/picojson.h"

int main() {
	std::string json = "[ \"hello JSON\" ]";
	picojson::value v;
	std::string err = picojson::parse(v, json);
	if (! err.empty()) {
		std::cerr << err << std::endl;
	}
	else
	{
		std::cout << v;
		std::cout << "Successfull"<<std::endl;
	}
}
