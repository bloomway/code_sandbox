package af.zoay.hrank.misc.regex.splitThePhoneNumbers;

import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
/*
 * ￼￼[Country code]-[Local Area Code]-[Number]
 */
public class SplitThePhoneNumbers {

	public static void main(String[] args) {
		System.out.println(new SplitThePhoneNumbers().splitThePhoneNumbers());
	}
	
	public String splitThePhoneNumbers()
	{
		StringBuilder phoneNumber = new StringBuilder();
		String data = 
		"/Applications/MAMP/htdocs/Zoay/HackrRank_Labsessions/src/af/zoay/hrank/misc/regex/splitThePhoneNumbers/splitPhoneNumbers.txt";
		
		String regex = "([0-9]{1,3})(-|\\s)([0-9]{1,3})(-|\\s)([0-9]{4,10})";
		Pattern p = Pattern.compile(regex);
		
		try(BufferedReader rd = new BufferedReader(new FileReader(new File(data))))
		{
			String firstline = rd.readLine();
			int n = Integer.parseInt(firstline);
			String line;
			if(1 <= n && n <= 20)
			{
				while((line = rd.readLine()) != null)
				{
					Matcher m = p.matcher(line.trim());
					if(m.find())
					{
						String sCountryCode = m.group(1);
						String sLocalAreaCode = m.group(3);
						String sNumber = m.group(5);
						
						String output = sCountryCode + ", " + sLocalAreaCode + ", "  + sNumber;
						phoneNumber.append(output).append("\n");
					}
				}
			}
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		
		return phoneNumber.toString();
	}
}
