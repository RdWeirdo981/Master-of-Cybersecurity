import java.util.ArrayList;
import java.util.Scanner;
/**
 * Write a description of class KoalaRescue here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class KoalaRescue
{
    // instance variables - replace the example below with your own
    private Reserve reserve; // import reserve class
    private RescueTeam team; // import team class

    /**
     * Constructor for objects of class KoalaRescue
     */
    public KoalaRescue()
    {
        reserve = new Reserve();
        team = new RescueTeam();
    }
    
    /**
     * Parametered Constructor for objects of class KoalaRescue
     */
    public KoalaRescue(Reserve reserve, RescueTeam team)
    {
        this.reserve = reserve;
        this.team = team;
    }

    /**
     * Method printWelcome
     * 
     * print a welcome message
     */
    public void printWelcome()
    {
        System.out.println("Welcome to the Koala rescue team.");
    }
    
    /**
     * Method setInitial
     * 
     * set team leader and initial budget
     */
    public void setTeam()
    {
        team.setLeaderName();
        team.setBudget();
    }
    
    /**
     * Method setReserve
     * 
     * initializes reserve
     */
    public void setReserve()
    {
        reserve.initialPoint();
    }
    
    /**
     * Method printTotalInfo
     * 
     * get and print observation point and team info
     */
    public void printTotalInfo(int index)
    {
        reserve.printInfo(index);
        System.out.println("Team budget: " + team.getBudget());
    }
    
    /**
     * Method takeAction
     * 
     * print the choices and enter A - D to take action
     */
    public boolean takeAction(int index)
    {
        System.out.println("\n");
        System.out.println("Please choose your action: ");
        System.out.println("A. Move an injured koala to the safe haven.(budget -$20)");
        System.out.println("B. Move an healthy koala to the safe haven.(budget -$10)");
        System.out.println("C. Relocate a koala to this place.(budget +$5)");
        System.out.println("D. Take no further action.");
        Scanner input = new Scanner(System.in);
        String action = input.nextLine();
        while (!action.equals("A") && !action.equals("B") && !action.equals("C") && !action.equals("D"))
        {
            System.out.println("Invalid Choice. Please enter again.");
            input = new Scanner(System.in);
            action = input.nextLine();
        }
        if (action.equals("A"))
        {
            moveInjured(index);
            return true;
        }
        else if (action.equals("B"))
        {
            moveHealthy(index);
            return true;
        }
        else if (action.equals("C"))
        {
            relocateKoala(index);
            return true;
        }
        else
        {
            return false; // take no action, move to the next observation point.
        }
    }
    
    /**
     * Method moveInjured
     * 
     * move an injured Koala to the safe haven
     */
    public void moveInjured(int index)
    {
        int newBudget = team.getBudget() - 20;
        boolean validBudget = team.validBuget(newBudget);
        boolean validInjured = reserve.validInjured(index);
        if (validBudget && validInjured)
        {
            team.moveInjuredCost();
            reserve.moveInjured(index);
        }
        else
        {
            System.out.println("\n");
            System.out.println("You can't take this action. Check your budget and the number of injured koalas. Try another.");
        }
    }
    
    /**
     * Method moveHealthy
     * 
     * move an healthy Koala to the safe haven
     */
    public void moveHealthy(int index)
    {
        int newBudget = team.getBudget() - 10;
        boolean validBudget = team.validBuget(newBudget);
        boolean validHealthy = reserve.validHealthy(index);
        if (validBudget && validHealthy)
        {
            team.moveHealthyCost();
            reserve.moveHealthy(index);
        }
        else
        {
            System.out.println("\n");
            System.out.println("You can't take this action. Check your budget and the number of healthy koalas. Try another.");
        }
    }
    
    /**
     * Method relocateKoala
     * 
     * relocate a Koala to original observation point
     */
    public void relocateKoala(int index)
    {
        boolean validCheck = reserve.validRelocate(index);
        if (validCheck)
        {
            reserve.relocateKoala(index);
            team.relocate();
        }
        else
        {
            System.out.println("\n");
            System.out.println("You can't take this action. Check the number of healthy koalas in safe haven. Try another.");
        }
    }
    
    /**
     * Method printOnePointFinish
     * 
     */
    public void printOnePointFinish(int index)
    {
        int deads = reserve.getOnePointDeads(index);
        int remainBudget = team.getBudget();
        System.out.println("\n");
        System.out.println("The number of dead Koalas is: " + deads);
        System.out.println("Remaining budget: " + remainBudget);
    }
    
    /**
     * Method printCompletion
     * 
     */
    public void printCompletion()
    {
        System.out.println("\n");
        System.out.println("All observation points have been gone through.");
        System.out.println("The total number of damaged trees: " + reserve.getTotalDamage());
        System.out.println("The total number of healthy koalas: " + reserve.getTotalHealthy());
        System.out.println("The total number of injured koalas: " + reserve.getTotalInjured());
        System.out.println("The total number of relocated koalas: " + reserve.getRelocates());
        System.out.println("The total amount spent: " + team.getAmountSpent());
    }
    
    /**
     * Method printSuccess
     */
    public void printSuccess()
    {
        int deads = reserve.getTotalDeads();
        if (reserve.getTotalDeads() == 0)
        {
            System.out.println("\n");
            System.out.println("Rescue was successful, with no koala deaths.");
        }
        else
        {
            System.out.println("Rescue completed with " + "'" + deads + "' " + "koalas deaths.");
        }
    }
    
    /**
     * Method writeUpdate
     * 
     * write update trees.txt
     */
    public void writeUpdate()
    {
        reserve.writeUpdate();
    }
    
    /**
     * Method startRescue
     * 
     * 
     */
    public void startRescue()
    {
        printWelcome();
        setTeam();
        reserve.initialPoint();
        for (int index = 0; index < 10; index++)
        {
            printTotalInfo(index);
            boolean ifRepeat = takeAction(index);
            while (ifRepeat)
            {
                printTotalInfo(index);
                ifRepeat = takeAction(index);
            }
            reserve.assessDead(index);
            printOnePointFinish(index);
        }
        printCompletion();
        printSuccess();
        writeUpdate();
    }
}
