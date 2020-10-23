# vault-door

Point: 50

## Category

Reverse Engineering

## Question

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java)

## Hint

The password is revealed in the program's source code.

## Solution

This challenge will need some programming knowledge to be able to read the source code and find out the flag from the java program given in the challenge.

Download the source code
```bash
wget https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java

cat VaultDoorTraining.java
```

```java
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals(""); //Flag was taken out to hide the solution.
    }
}
```

The java program above is fairly simple to comprehend. It has one main function that checks for the password and prefixes the user input check with **picoCTF{** and another function to check for the flag inside the brackets.

compile & run the program and the correct flag will return **Access granted** as below.
```bash
javac VaultDoorTraining.java
java VaultDoorTraining
Enter vault password: picoCTF{correctsolution}
Access granted.
```

## Improvement

Upon further playing around with the program, a flaw is observed in such a way that, the program is only checking the contents inside the **checkPassword()** function with the prefix **picoCTF{**. The closing bracket **}** is not properly checked. Any character can be entered to match the length of the flag to get back **Access granted.** prompt as below.

```bash
java VaultDoorTraining
Enter vault password: picoCTF{correctsolution]
Access granted.
```