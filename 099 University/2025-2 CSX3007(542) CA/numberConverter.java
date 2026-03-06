 
import java.util.Scanner;
 
public class numberConverter {
 
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Number Convert");
 
        while (true) {
            System.out.println("\nSelect a conversion type:");
            System.out.println("1. Decimal to Binary");
            System.out.println("2. Binary to Decimal");
            System.out.println("3. Decimal to Hexadecimal");
            System.out.println("4. Binary to Hexadecimal");
            System.out.println("5. Hexadecimal to Decimal");
            System.out.println("6. Exit");
            System.out.print("Enter your choice (1-6): ");
 
            if (scanner.hasNextInt()) {
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline
 
                try {
                    switch (choice) {
                        case 1:
                            System.out.print("Enter Decimal number: ");
                            int dec1 = scanner.nextInt();
                            System.out.println("Binary: " + Integer.toBinaryString(dec1));
                            break;
                        case 2:
                            System.out.print("Enter Binary number: ");
                            String bin1 = scanner.nextLine();
                            int dec2 = Integer.parseInt(bin1, 2);
                            System.out.println("Decimal: " + dec2);
                            break;
                        case 3:
                            System.out.print("Enter Decimal number: ");
                            int dec3 = scanner.nextInt();
                            System.out.println("Hexadecimal: " + Integer.toHexString(dec3).toUpperCase());
                            break;
                        case 4:
                            System.out.print("Enter Binary number: ");
                            String bin2 = scanner.nextLine();
                            // binary to decimal then decimal to hex
                            int dec_from_bin = Integer.parseInt(bin2, 2);
                            System.out.println("Hexadecimal: " + Integer.toHexString(dec_from_bin).toUpperCase());
                            break;
                        case 5:
                            System.out.print("Enter Hexadecimal number: ");
                            String hex1 = scanner.nextLine();
                            int dec5 = Integer.parseInt(hex1, 16);
                            System.out.println("Decimal: " + dec5);
                            break;
                        case 6:
                            System.out.println("Exited.");
                            return;
                        default:
                            System.out.println("Invalid choice. Please enter a number between 1 and 6.");
                    }
                } catch (java.util.InputMismatchException e) {
                    System.out.println("Invalid input. Please enter a number as requested.");
                    scanner.nextLine();
                } catch (NumberFormatException e) {
                    System.out.println("Invalid number format for the selected base.");
                }
            } else {
                System.out.println("Invalid choice. Please enter a number.");
                scanner.next();
            }
            }
        }
    }
}
 
 