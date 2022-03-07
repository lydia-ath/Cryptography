/**
 * Authors
 * Athanasiou Lydia
 * Christodoulakis Giorgos
 * Drougka Sofia
 * */

package vigenerCipher;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class VigenerCipher {
	
	 public static void main(String arg[]){
		 
		 String filePath = "plaintext.txt";
		 
		 String ptext = readMessage( filePath); 
		 
		 System.out.println("Message from file: "+ptext);
		 ptext = ptext.replaceAll("\\s", "");
		 System.out.println("Message without spaces: "+ptext); 
		 
		 String plaintext = readMessage( filePath); 
		 
		 plaintext =  plaintext.replaceAll("\\s", "");
		 
		 String keyword = "LASDIEGO";
		 
		 String ciphertext = encryptToCipherText(plaintext,keyword);
		 
		 String decrypted_plaintext = decryptToPlainText(ciphertext, keyword);
		 
		 printResults(plaintext, ciphertext, decrypted_plaintext, keyword);
	 
	 }
  
	 public static String encryptToCipherText(String plaintext, String keyword){
		 
		 //Convert plaintext to char array
		 char msg[] = plaintext.toCharArray();
		 
		 // key and encrypted message to char arrays
		 int msgLen = msg.length;
		 
		 char encryptedMsg[] = new char[msgLen];
		 char key[] = keyFix(keyword, msgLen);
	  
		 //encryption code 
		 String ciphertext = "";
		 for(int i = 0; i < msgLen; ++i) {
		 		 
			 encryptedMsg[i] = (char) (((msg[i] + key[i]) % 26) + 'A');
			 ciphertext += encryptedMsg[i];
		 }
		 
		 return ciphertext;
	 
	 }
	 
	 public static String decryptToPlainText(String ciphertext, String keyword) {
		 
		//Convert ciphertext to char array
		 char encryptedMsg[] = ciphertext.toCharArray();
		 
		 int msgLen = encryptedMsg.length;
		 
		 char decryptedMsg[] = new char[msgLen];
		 char key[] = keyFix(keyword, msgLen);
		 
		//decryption code
		 String plaintext = "";
		 for(int i = 0; i < msgLen; ++i) {
			 
			decryptedMsg[i] = (char)((((encryptedMsg[i] - key[i]) + 26) % 26) + 'A');
		 	plaintext += decryptedMsg[i];
		 	
		 }

		 return plaintext;
	  }
	 
	 /*The function keyFix extends length of the keyword based on plaintext's length*/
	 private static char[] keyFix(String keyword, int msgLen) {
		 
		 int i,j;
		 
		 char key[] = new char[msgLen];
		 
		 for(i = 0, j = 0; i < msgLen; ++i, ++j){
			if(j == keyword.length()){
				j = 0;
			}
			key[i] = keyword.charAt(j);
		 }
		
		 return key; 
	 }
	 
	 private static void printResults(String plaintext, String ciphertext, String decrypted_plaintext, String keyword) {
		 
		 System.out.println("Original Message: " + plaintext);  
		 System.out.println("Character length: " + plaintext.length());
		 System.out.println("Keyword: " + keyword);
		 
		 char[] key = keyFix(keyword, plaintext.length());
		 System.out.println("Key: " + String.valueOf(key));
		 System.out.println();
		 
		 System.out.println("Encrypted Message: " + ciphertext);
		 System.out.println();      
	
		 System.out.println("Decrypted Message: " + decrypted_plaintext);
		 
	 }
		 
	 private static String readMessage(String filePath) {
	     StringBuilder stringBuilder = new StringBuilder();
	     try (BufferedReader br = new BufferedReader(new FileReader(filePath))){
	
	         String sCurrentLine;
	         while ((sCurrentLine = br.readLine()) != null) {
	        	 stringBuilder.append(sCurrentLine).append("\n");
	         }
	           
	     } 
	     catch (IOException e) {
	         e.printStackTrace();
	     }
	        
	     return stringBuilder.toString().toUpperCase();
	 }
}
