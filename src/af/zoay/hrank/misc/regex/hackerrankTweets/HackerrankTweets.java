package af.zoay.hrank.misc.regex.hackerrankTweets;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class HackerrankTweets {
	
	private static final String data =
			"/Applications/MAMP/htdocs/Zoay/HackrRank_Labsessions/src/af/zoay/hrank/misc/regex/hackerrankTweets/hackerrankTweets.txt";
	private String regex = "(h|H)(a|A)(c|C)(k|K)(e|E)(r|R)(r|R)(a|A)(n|N)(k|K)";
	public static void main(String[] args)
	{
		System.out.println(new HackerrankTweets().findAllHrankInTweets());
	}
	
	public int findAllHrankInTweets()
	{
		int count = 0;
		
		try(BufferedReader rd = new BufferedReader(new FileReader(new File(data))))
		{
			String firstline = rd.readLine();
			int n = Integer.parseInt(firstline);
			
			if(1 <= n && n <= 10)
			{
				String line;
				Pattern p = Pattern.compile(regex);
				while((line = rd.readLine()) != null)
				{
					Matcher m = p.matcher(line);
					if(m.find()) count++;
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
		return count;
	}
}
