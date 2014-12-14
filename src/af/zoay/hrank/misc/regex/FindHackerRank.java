package af.zoay.hrank.misc.regex;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class FindHackerRank {
	/*
	 * N: numbers of lines
	 * W: numbers of words, separated by a single space
	 * C: count of the characters in a word(W)
	 * 
	 * Constraints:
	 * 1 <= N <= 10
	 * 1 <= W <= 100
	 * 1 <= C <= 20
	 */
	public static final String HACKERRANK = "hackerrank";
	public static void main(String[] args)
	{
		System.out.println(new FindHackerRank().findHackerRank());
	}
	
	public FindHackerRank()
	{
		
	}
	
	public String findHackerRank()
	{
		StringBuilder sb = new StringBuilder();
		
		try(BufferedReader reader = new BufferedReader(new FileReader(new File("/Applications/MAMP/htdocs/Zoay/HackrRank_Labsessions/src/af/zoay/hrank/misc/regex/hrank_regex.txt"))))
		{
			String line;
			String firstLine = reader.readLine();
			int N = Integer.parseInt(firstLine);
			
			while((line = reader.readLine()) != null)
			{
				//System.out.println(line);
				
				if(N>=1 && N<=10)
				{
					if ( !(line.startsWith(HACKERRANK)) && !(line.endsWith(HACKERRANK)) ) sb.append("-1").append("\n");
					else
					{
						if(line.startsWith(HACKERRANK)) 
						{
							if(line.endsWith(HACKERRANK)) sb.append("0").append("\n");
							else sb.append("1").append("\n");
						}
						else if(line.endsWith(HACKERRANK)) sb.append("2").append("\n");
					}
				}
			}
			
			//System.out.println(sb.toString());
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
