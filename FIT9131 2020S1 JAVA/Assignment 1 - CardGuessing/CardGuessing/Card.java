/**
 * This is the Card class.This class will specify the attributes and behaviour of card.
 *
 * @due on 2020-05-07
 */
public class Card
{
    // fields
    private int suit;
    private int number;
    private String suitNumber;
    private RandomNumber rs;
    private RandomNumber rn;

    /**
     * Constructor for objects of class Card
     */
    public Card()
    {
        // default constructor
        suit = 0;
        number = 0;
        suitNumber = "00";
    }
    
    public Card(int suit, int number)
    {
        // parametered constructor
        this.suit = suit;
        this.number = number;
        recSuitNumber();
    }

    /**
     * display suit and number
     *
     */
    public String recSuitNumber()
    {
        String suitString = "";
        switch (suit)
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
                System.out.println("Invilid value.");
                break;
        }
        String no = String.valueOf(number);
        suitString = suitString + no;
        return suitString;
    }
    
    /**
     * get card suit
     */
    public int getCardSuit()
    {
        return suit;
    }
    
    /**
     * get card number
     */
    public int getCardNumber()
    {
        return number;
    }
    
    /**
     * get a random card suit
     *
     */
    public void getSuit()
    {
        rs = new RandomNumber(3);
        suit = rs.getRandom() + 1;
    }
    
    /**
     * get a random card number
     *
     */
    public void getNumber()
    {
        rn = new RandomNumber(12);
        number = rn.getRandom() + 1;
    }
}