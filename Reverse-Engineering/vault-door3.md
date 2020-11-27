# vault-door3

Point: 200

## Category

Reverse Engineering

## Question

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a4018cec1446761cb2e8cce05db925fa/VaultDoor3.java)

## Hint

Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

## Solution

This was a fairly difficult challenge to tackle. The hint given was a great starting point to try to reverse engineer the password from the source code.

The original source code is given as below
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }

        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
    }
}
```
From the checkPassword() function, the user input is being compared to a string. Intuitively, that string is used to see if it's a correct flag with no success.

```bash
javac VaultDoor3.java && java VaultDoor3
Enter vault password: picoCTF{jU5t_a_sna_3lpm12g94c_u_4_m7ra41}
Access denied!
```
After some googling around and as given by the hint, a separate function is written to reverse engineer the password as below.

```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        vaultDoor.reverseEngineerPw();   // NEW FUNCTION ADDED HERE
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public void reverseEngineerPw() {
        String password = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41";
        char[] buffer = new char[32];
        int i;

        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }

        String s = new String(buffer);
        System.out.println("picoCTF{" + s + "}");
    }
```

The function essentially re-arranges the string comparison given in the source code to the correct flag.
```bash
javac VaultDoor3.java && java VaultDoor3
picoCTF{correctsolution}
Enter vault password: picoCTF{correctsolution}
Access granted.
```

## Improvement
None
