import java.util.Scanner;

/**
 * This is the Player class.This class will specify the attributes and behaviour of a player.
 *
 * @due on 2020-05-07
 */
public class Player
{
    // fields of player
    private String name;
    private int score;
    private int guess;
    private int hScore;
    private int numberOfGamesPlayed;
    private int numberOfGamesWon;

    /**
     * Default constructor for objects of class Player
     */
    public Player()
    {
        name = "";
        score = 40;
        guess = 0;
        hScore = 0;
        numberOfGamesPlayed = 0;
        numberOfGamesWon = 0;
    }
    
    /**
     * parametered constructor for objects of class Player
     */
    public Player(String name)
    {
        this.name = name;
        score = 40;
        guess = 0;
        hScore = 0;
        numberOfGamesPlayed = 0;
        numberOfGamesWon = 0;
    }
    
    /**
     * get player's name
     */
    public String getName()
    {
        return name;
    }
    
    /**
     * get player's current score
     */
    public int getScore()
    {
        return score;
    }
    
    /**
     * get player's last guess
     */
    public int getGuess()
    {
        return guess;
    }
    
    /**
     * get player's hightest score
     */
    public int getHScore()
    {
        return hScore;
    }
    
    /**
     * get player's number Of Games Played
     */
    public int getNOGP()
    {
        return numberOfGamesPlayed;
    }
    
    /**
     * get player's numberOfGamesWon
     */
    public int getNOGW()
    {
        return numberOfGamesWon;
    }
    
    /**
     * set player's last guess
     */
    public void setGuess(int gs)
    {
        guess = gs;
    }
    
    /**
     * set player's score
     */
    public void setScore(int sc)
    {
        score = score + sc;
    }
    
    /**
     * set player's highest score
     */
    public void setHScore(int hs)
    {
        hScore = hs;
    }
    
    /**
     * set number of game played
     */
    public void updateGamePlayed()
    {
        numberOfGamesPlayed++;
    }
    
    /**
     * set number of game won
     */
    public void updateGameWon()
    {
        numberOfGamesWon++;
    }
}
