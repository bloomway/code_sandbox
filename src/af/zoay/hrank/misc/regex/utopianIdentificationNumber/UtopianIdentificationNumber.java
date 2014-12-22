package af.zoay.hrank.misc.regex.utopianIdentificationNumber;

import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class UtopianIdentificationNumber {
	
	public static final String VALID = "VALID";
	public static final String INVALID = "INVALID";
	
	public static void main(String[] args) {
		System.out.println(new UtopianIdentificationNumber().validUIN());
	}

	public final String validUIN()
	{
		String regex = "^[a-z]{0,3}\\d{2,8}[A-Z]{3,}$";
		Pattern p = Pattern.compile(regex);
		String data = 
		"/Applications/MAMP/htdocs/Zoay/HackrRank_Labsessions/src/af/zoay/hrank/misc/regex/utopianIdentificationNumber/uni.txt";
		
		StringBuilder status = new StringBuilder();
		try(BufferedReader r = new BufferedReader(new FileReader(new File(data))))
		{
			String firstLine = r.readLine();
			int n = Integer.parseInt(firstLine);
			Matcher m  = null;
			if(1 <= n && n <= 100)
			{
				String line;
				while((line = r.readLine()) != null)
				{
					m = p.matcher(line);
					if(m.find()) status.append(VALID).append("\n");
					else status.append(INVALID).append("\n");
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
		return status.toString();
	}
}
