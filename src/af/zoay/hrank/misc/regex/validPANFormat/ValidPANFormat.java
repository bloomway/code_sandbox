package af.zoay.hrank.misc.regex.validPANFormat;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 * PAN Number format
 * <char><char><char><char><char><digit><digit><digit><digit><char> 
 * 
 * 	Input Format
 *	First line contains N. N lines follow, each having a PAN number.
 *
 *	Constraints
 *	1 <= N <= 10
 *	Each letter is an uppercase letter. Each digit lies between 0 and 9
 *	The length of the PAN number is always 10
 *	Every character in PAN is either char or digit satisfying the above constraints.
 *	
 *	Output Format
 *	For every PAN number listed, print YES if it is valid and NO if it isn't.
 */

public class ValidPANFormat {
	
	public static final String YES = "YES";
	public static final String NO = "NO";
	
	public static void main(String[] args)
	{
		System.out.println(new ValidPANFormat().validPANFormat());
	}
	
	public String validPANFormat()
	{
		StringBuilder sb = new StringBuilder();
		
		try(BufferedReader rd = new BufferedReader(new FileReader(new File("/Applications/MAMP/htdocs/Zoay/HackrRank_Labsessions/src/af/zoay/hrank/misc/regex/validPANFormat/validPANFormat.txt"))))
		{
			String firstline = rd.readLine();
			int N = Integer.parseInt(firstline);
			String line;
			
			if( 1<= N && N<= 10)
			{
				String regex = "[A-Z]{5}\\d{4}[A-Z]";
				Pattern pattern = Pattern.compile(regex);
	
				while((line = rd.readLine()) != null)
				{
					Matcher m = pattern.matcher(line);
					if(m.find()) sb.append(YES).append("\n");
					else sb.append(NO).append("\n");
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
		return sb.toString();
	}
}
