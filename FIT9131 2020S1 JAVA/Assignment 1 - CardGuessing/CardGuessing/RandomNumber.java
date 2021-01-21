import java.util.Random;
/**
 * generate random number
 *
 * @due on 2020-05-07
 */
public class RandomNumber
{
    // max limit
    private int max;
    private int rand;

    /**
     * Default constructor for objects of class RandomNumber
     */
    
    public RandomNumber()
    {
        max = 0;
    }
    
    /**
     * parametered constructor for objects of class RandomNumber
     */
    public RandomNumber(int max)
    {
        // the upper limit of the range of the random number
        this.max = max;
    }

    /**
     * generate a random number from 0 to max
     *
     */
    public int getRandom()
    {
        // user input a number
        Random rn = new Random();
        rand = rn.nextInt(max)+1;
        return rand;
    }
}
