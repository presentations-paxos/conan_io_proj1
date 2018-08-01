#include <proj1/hello.hpp>

#include <boost/format.hpp>
#include <sstream>

namespace proj1 {

    std::string hello(const std::string& name) {

        std::stringstream ss;
        ss << boost::format("Hello, %s") % name;

        return ss.str();
    }
}
