🔍 Advanced Python Port Scanner

An enhanced Port Scanner built using Python, offering more flexibility with custom port range scanning, improved input validation, and user-friendly terminal output. It is ideal for those who are beginning to explore network scanning in depth.




📌 Learning Objectives

-Understand advanced socket programming concepts.

-Customize port scanning ranges for flexibility.

-Improve user input handling and validations.

-git add advanced_port_scanner/README.md
git commit -m "Add README.md for advanced port scanner"
git push origin mainMeasure scan performance using timestamps.





🚀 Features

-Scan specific IP addresses within user-defined port ranges

-Input validation for both IP format and port values

-Displays total number of open ports found

-Execution time tracking

-Clean CLI-based interface





🛠 Technologies Used

-Python 3

-socket module

-time module

-Input validation with try-except blocks





🧪 Example Output

Enter the IP address to scan: 127.0.0.1
Enter start port (e.g., 20): 30
Enter end port (e.g., 80): 99
Scanning 127.0.0.1 from port 30 to 99...

Scan complete.
Total Open Ports: 0
Time Taken: 35.67 seconds




🔮 Future Enhancements

-Add multi-threading to improve scan speed

-Integrate banner grabbing to identify running services

-Include progress bar or UI for better user experience

-Export scan results to CSV/JSON

-Add support for scanning multiple IPs in batch





📂 File Structure

advanced_port_scanner.py     # Main scanner script with user-defined port input
README.md                    # Project documentation