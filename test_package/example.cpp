#include <iostream>
#include "spdlog/spdlog.h"

int main(int, char* [])
{
    try
    {         
         //Multithreaded console logger(with color support)
        auto console = spdlog::stdout_logger_mt("console", true /*use color*/);
        console->info("Welcome to spdlog!") ;
        console->info("An info message example {} ..", 1);
        console->info() << "Streams are supported too  " << 2;
        // create a file rotating logger with 5mb size max and 3 rotated files
        auto file_logger = spdlog::rotating_logger_mt("file_logger", "myfilename", 1024 * 1024 * 5, 3);
        file_logger->info("Hello spdlog {} {} {}", 1, 2, "three");

    }
    catch (const spdlog::spdlog_ex& ex)
    {
        std::cout << "Log failed: " << ex.what() << std::endl;
    }
}