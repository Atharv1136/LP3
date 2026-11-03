// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure
    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    // Array
    Student[] public students;

    // Add student
    function addStudent(uint _rollNo, string memory _name, uint _marks) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    // Get student details
    function getStudent(uint _index) public view returns (uint, string memory, uint) {
        require(_index < students.length, "Invalid index");

        Student memory s = students[_index];

        return (s.rollNo, s.name, s.marks);
    }

    // Get student count
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Receive Ether
    receive() external payable {
    }

    // Fallback function
    fallback() external payable {
    }
}