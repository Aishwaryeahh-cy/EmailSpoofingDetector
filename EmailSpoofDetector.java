// Source code is decompiled from a .class file using FernFlower decompiler.
import java.util.Scanner;

public class EmailSpoofDetector {
   public EmailSpoofDetector() {
   }

   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      System.out.print("Enter the sender's domain (e.g., mail.google.com): ");
      String var2 = var1.nextLine().trim().toLowerCase();
      System.out.print("Enter the 'From' email address (e.g., user@gmail.com): ");
      String var3 = var1.nextLine().trim().toLowerCase();
      var1.close();
      String var4 = getDomainFromEmail(var3);
      if (var2.contains(var4)) {
         System.out.println("âœ… No spoofing detected. Sender domain matches 'From' email.");
      } else {
         System.out.println(" Possible spoofing detected! Domains do not match.");
      }

   }

   private static String getDomainFromEmail(String var0) {
      return var0.contains("@") ? var0.substring(var0.indexOf("@") + 1) : "";
   }
}
