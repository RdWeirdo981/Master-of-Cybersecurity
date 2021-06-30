import java.util.Scanner;
import java.util.InputMismatchException;
/**
 * This class is for recording the infomation of the recue team.
 *
 * @06-07-2020
 */
public class RescueTeam
{
    // instance variables - replace the example below with your own
    private String leaderName; // a name. can't be blank and len < 16
    private int budget; // a number from 100 to 200 inclusive
    private int originalBudget;

    /**
     * Constructor for objects of class RescueTeam
     */
    public RescueTeam()
    {
        leaderName = "Empty";
        budget = 0;
        originalBudget = 0;
    }
    
    /**
     * Parametered Constructor
     * 
     * para: 
     */
    public RescueTeam(String leader, int budgetAmount, int origin)
    {
        leaderName = leader;
        budget = budgetAmount;
        originalBudget = origin;
    }

    /**
     * Method getLeaderName
     * 
     * return a String of leader's name
     */
    public String getLeaderName()
    {
        return leaderName;
    }
    
    /**
     * Method getBudget
     * 
     * return a double number of budget
     */
    public int getBudget()
    {
        return budget;
    }
    
    /**
     * Method getBudget
     * 
     * return a double number of budget
     */
    public int getOrigin()
    {
        return originalBudget;
    }
    
    /**
     * Method setLeaderName
     * 
     * use Scanner to get a leader's name
     * validation: can't blank, can't > 16, must be a String
     */
    public void setLeaderName()
    {
        System.out.println("Please enter the leader's name, which should be less than 16 characters and not blank.");
        Scanner input = new Scanner(System.in);
        String name = input.nextLine();
        boolean validCheck = isAlphabetic(name);
        while(!validCheck || (validCheck && name.length() >= 16))
        {
            System.out.println("Invalid input. Please check the condition and enter again.");
            input = new Scanner(System.in);
            name = input.nextLine();
            validCheck = isAlphabetic(name);
        }
        input.close();
        leaderName = name;
    }
    
    /**
     * Method isAlphabetic
     * 
     */
    public boolean isAlphabetic(String string)
    {
        if (string.length() == 0)
        {
            return false;
        }
        int n = 0;
        while(n < string.length())
        {
            char ch = string.charAt(n);
            if ((ch < 'A') || (ch > 'Z' && ch < 'a') || (ch > 'z'))
            {
                return false;
            }
            else
            {
                n++;
            }
        }
        return true;
    }
    
    /**
     * Method isNumericString
     * 
     * a method to judge if a String is numric
     */
    public boolean isNumericString(String string)
    {
        if (string.length() == 0)
        {
            return false;
        }
        int n = 0;
        while(n < string.length())
        {
            char ch = string.charAt(n);
            if (ch < '0' || ch > '9')
            {
                return false;
            }
            else
            {
                n++;
            }
        }
        return true;
    }
    
    /**
     * Method setBudget
     * 
     * set the team's budget
     */
    public void setBudget()
    {
        System.out.println("Please enter the budget, which should be a double number of 100 to 200, inclusive.");
        Scanner input = new Scanner(System.in);
        String amount = input.nextLine();
        boolean validCheck = isNumericString(amount);
        if (!validCheck)
        {
            System.out.println("Invalid input. Please check the condition and enter again.");
            setBudget();
        }
        else if (validCheck && (Integer.parseInt(amount) < 100 || Integer.parseInt(amount) > 200))
        {
            System.out.println("Invalid input. Please check the condition and enter again.");
            setBudget();
        }
        else
        {
            input.close();
            budget = Integer.parseInt(amount);
            originalBudget = Integer.parseInt(amount);
        }
    }
        
    /**
     * Method printInfo
     * 
     * print team info
     */
    public void printInfo()
    {
        System.out.println("Team leader: " + leaderName);
        System.out.println("Team budget: " + budget);
        System.out.println("\n");
    }
    
    /**
     * Method changeBudget
     * 
     * change budget by a given number
     */
    public boolean validBuget(int newBudget)
    {
        if (newBudget >= 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    
    /**
     * Method moveInjuredCost
     * 
     * change budget when move injured Koals
     */
    public void moveInjuredCost()
    {
        budget -= 20;
    }
    
    /**
     * Method moveHealthyCost
     * 
     * change budget when move healthy Koals
     */
    public void moveHealthyCost()
    {
        budget -= 10;
    }
    
    /**
     * Method relocate
     * 
     * change budget when relocate a koala
     */
    public void relocate()
    {
        budget += 5;
    }
    
    /**
     * Method getAmountSpent
     * 
     */
    public int getAmountSpent()
    {
        int spent = budget - originalBudget;
        return spent;
    }
}
