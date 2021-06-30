
import java.util.Scanner;
import java.util.*;

/**
 * This is the Game class.This class will manage the game.
 *
 * @due on 2020-05-07
 */
public class Game
{
    //fields
    private Player cardGamePlayer;
    private Card hiddenCard;
    private int noOfAttemptSuit;
    private int noOfAttemptNo;
    private int gameScore;
    private int suit;
    private int number;
    private int countScore;
    
    /**
     * Constructor for objects of class Game
     */
    public Game()
    {
        // initialise the fields
        cardGamePlayer = new Player();
        hiddenCard = new Card();
        noOfAttemptSuit = 0; 
        noOfAttemptNo = 0;
        gameScore = 40;
        suit = 0;
        number = 0;
        countScore = 0;
    }

    /**
     * Display a welcome message on the screen
     *
     */
    public void displayMessage()
    {
        System.out.println("Wellcome to the game!"+"\n");
    }
    
    /**
     * Request the player to enter their name.
     *
     */
    public void enterName()
    {
        System.out.println("Please enter your name: ");
        Scanner pn = new Scanner(System.in);
        String name = pn.nextLine();
        cardGamePlayer = new Player(name);
        System.out.println("Your name is: "+ cardGamePlayer.getName());
    }
    
    /**
     * Request the player to enter a suit.
     *
     */
    public void enterSuit()
    {
        System.out.println("Please enter your suit. "+ "\n");
        System.out.println("H for heart, D for diamond, C for club, S for spade. "+ "\n");
        Scanner gs = new Scanner(System.in);
        String guessSuit = gs.nextLine();
        if (guessSuit.equals("H") || guessSuit.equals("D") || guessSuit.equals("C") || guessSuit.equals("S"))
        {
            suit = convertSTI(guessSuit);
        }
        else
        {
            System.out.println("invalid value. Type again."+ "\n");
            enterSuit();
        }
        cardGamePlayer.setGuess(suit);
    }
    
    /**
     * Convert String to Int
     *
     */
    public int convertSTI(String suitString)
    {
        int suitInt = 0;
        switch (suitString)
        {
            case "H": 
                suitInt = 1; break;
            case "D":
                suitInt = 2; break;
            case "C":
                suitInt = 3; break;
            case "S":
                suitInt = 4; break;
            default:
                break;
        }
        return suitInt;
    }
    
    /**
     * Convert Int to String
     *
     */
    public String convertITS(int suitInt)
    {
        String suitString = "";
        switch (suitInt)
        {
            case 1: 
                suitString = "H"; break;
            case 2:
                suitString = "D"; break;
            case 3:
                suitString = "C"; break;
            case 4:
                suitString = "S"; break;
            default:
                break;
        }
        return suitString;
    }
  
    /**
     * Request the player to enter a card number.
     *
     */
    public void enterNumber()
    {
        System.out.println("Please enter your card number between 1-13: ");
        Scanner gn = new Scanner(System.in);
        try
        {
            number = gn.nextInt();
            if ((number > 13) || (number < 1))
            {
                System.out.println("Invalid value. Try again." + "\n");
                enterNumber();
            }
            else
            {
                cardGamePlayer.setGuess(number);
            }
        }
        catch (InputMismatchException e)
        {
            System.out.print("Invalid value. Try again." + "\n");
            enterNumber();
        }
    }

    /**
     * Compare the suit entered by a player with the hidden suit.
     *
     */
    public void compareSuit(int hiddenSuit)
    {
        noOfAttemptSuit = 1;
        String hiddenSuitString = convertITS(hiddenSuit);
        while(noOfAttemptSuit <= 3 && cardGamePlayer.getScore()>0)
        {
            if (suit == hiddenSuit)
            {
                displayAttemptsSuit();
                System.out.println("Corrent. Move to the next."+"\n");
                return; 
            }
            else if (suit != hiddenSuit && noOfAttemptSuit == 1)
            {
                displayAttemptsSuit();
                System.out.println("Wrong. Try again."+"\n");
                countScore -= 5;
                cardGamePlayer.setScore(-5);
                noOfAttemptSuit++;
                enterSuit();
            }
            else if (suit != hiddenSuit && noOfAttemptSuit == 2)
            {
                displayAttemptsSuit();
                System.out.println("Wrong. Try again."+"\n");
                countScore -= 10;
                cardGamePlayer.setScore(-10);
                noOfAttemptSuit++;
                enterSuit();
            }
            else if (suit != hiddenSuit && noOfAttemptSuit == 3)
            {
                displayAttemptsSuit();
                System.out.println("Wrong. The correct suit is: " + hiddenSuitString);
                countScore -= 15;
                cardGamePlayer.setScore(-15);
                noOfAttemptSuit++;
            }    
        }
        if (cardGamePlayer.getScore()<=0)
        {
            System.out.println("The hidden card is: " + hiddenCard.recSuitNumber() + "\n");
            System.out.println("You've run out of the score.");
            System.out.println("Game Over.");
            System.out.println("Total number of game played: " + cardGamePlayer.getNOGP());
            System.out.println("Total number of game won: " + cardGamePlayer.getNOGW());
            System.out.println("The highest score is: " + cardGamePlayer.getHScore());
            System.exit(0);
        }
    }
                
    /**
     * Compare the number entered by a player with the hidden number.
     *
     */
    public void compareNumber(int hiddenNo)
    {
        noOfAttemptNo = 1;
        while(noOfAttemptNo <= 4 && cardGamePlayer.getScore()>0)
        {
            if (number == hiddenNo)
            {
                displayAttemptsSNumber();
                System.out.println("Corrent. You win.");
                cardGamePlayer.updateGameWon();
                return;
            }
            else if (number != hiddenNo && noOfAttemptNo == 1)
            {
                displayAttemptsSNumber();
                System.out.println("Wrong. Try again.");
                countScore -= 2;
                cardGamePlayer.setScore(-2);
                noOfAttemptNo++;
                enterNumber();
            }
            else if (number != hiddenNo && noOfAttemptNo == 2)
            {
                displayAttemptsSNumber();
                System.out.println("Wrong. Try again.");
                countScore -= 6;
                cardGamePlayer.setScore(-6);
                noOfAttemptNo++;
                enterNumber();
            }
            else if (number != hiddenNo && noOfAttemptNo == 3)
            {
                displayAttemptsSNumber();
                System.out.println("Wrong. Try again.");
                countScore -= 12;
                cardGamePlayer.setScore(-12);
                noOfAttemptNo++;
                enterNumber();
            }
            else if (number != hiddenNo && noOfAttemptNo++ == 4)
            {
                displayAttemptsSNumber();
                System.out.println("Wrong. You lose.");
                System.out.println("The hidden card is: " + hiddenCard.recSuitNumber());
                countScore -= 15;
                cardGamePlayer.setScore(-15);
                noOfAttemptNo++;
            }
        } 
        if (cardGamePlayer.getScore()<=0)
        {
            System.out.println("The hidden card is: " + hiddenCard.recSuitNumber() + "\n");
            System.out.println("You've run out of the score.");
            System.out.println("Game Over.");
            System.out.println("Total number of game played: " + cardGamePlayer.getNOGP());
            System.out.println("Total number of game won: " + cardGamePlayer.getNOGW());
            System.out.println("The highest score is: " + cardGamePlayer.getHScore());
            System.exit(0);
        }
    }
    
    /**
     * Compare the number entered by a player with the hidden number.
     *
     */
    public void singleGame()
    {
        gameScore += countScore;
        if (gameScore > cardGamePlayer.getHScore())
        {
            cardGamePlayer.setHScore(gameScore);
        }
        System.out.println("The score for this game is: " + gameScore);
        System.out.println("The overall score for all game is: " + cardGamePlayer.getScore());
    }
    
    /**
     * Compare the number entered by a player with the hidden number.
     *
     */
    public void initialScore()
    {
        gameScore = 40;
        countScore = 0;
        cardGamePlayer.setScore(40);
    }
    
    /**
     * Display the result of the attempt at guessing the suit.
     *
     */
    public void displayAttemptsSuit()
    {
        System.out.println("Number of Attempts of Suit is: " + noOfAttemptSuit);
    }
    
    /**
     * Display the result of the attempt at guessing the number.
     *
     */
    public void displayAttemptsSNumber()
    {
        System.out.println("Number of Attempts of Number is: " + noOfAttemptNo);
    }
    
    /**
     * Display the overall result when the player decides to stop playing.
     *
     */
    public void repeatGame()
    {
        Scanner rg = new Scanner(System.in);
        String YorN = rg.nextLine();
        if (YorN.equals("Y"))
        {
            afterGame();
        }
        else if (YorN.equals("N"))
        {
            System.out.println("Game Over.");
            System.out.println("Total number of game played: " + cardGamePlayer.getNOGP());
            System.out.println("Total number of game won: " + cardGamePlayer.getNOGW());
            System.out.println("The highest score is: " + cardGamePlayer.getHScore());
            return;
        }
        else
        {
            System.out.println("Invalid choice. Please enter Y or N.");
            repeatGame();
        }
    }
            
    /**
     * play game
     *
     */
    public void playGame()
    {
        displayMessage();
        enterName();
        hiddenCard.getSuit();
        hiddenCard.getNumber();
        enterSuit();
        compareSuit(hiddenCard.getCardSuit());
        enterNumber();
        compareNumber(hiddenCard.getCardNumber());
        singleGame();
        cardGamePlayer.updateGamePlayed();
        System.out.println("Continue? Y/N"+"\n");
        repeatGame();
    }
    
    /**
     * play the game behind first game
     *
     */
    public void afterGame()
    {
        initialScore();
        displayMessage();
        hiddenCard.getSuit();
        hiddenCard.getNumber();
        enterSuit();
        compareSuit(hiddenCard.getCardSuit());
        enterNumber();
        compareNumber(hiddenCard.getCardNumber());
        singleGame();
        cardGamePlayer.updateGamePlayed();
        System.out.println("Continue? Y/N"+"\n");
        repeatGame();
    }
}
