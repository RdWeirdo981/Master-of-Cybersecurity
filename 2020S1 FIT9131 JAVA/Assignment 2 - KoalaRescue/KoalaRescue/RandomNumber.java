import java.util.Random;
/**
 * generate random number
 *
 * @06-07-2020
 */
public class RandomNumber
{
    private int max;

    /**
     * Default constructor for objects of class RandomNumber
     */
    
    public RandomNumber()
    {
        max = 1;
    }
    
    /**
     * parametered constructor for objects of class RandomNumber
     */
    public RandomNumber(int maxNumber)
    {
        max = maxNumber;
    }
    
    /**
     * Method setMax
     * 
     * set the max number of this random generator
     */
    public void setMax(int maxNumber)
    {
        max = maxNumber;
    }

    /**
     * Method getRandom
     * 
     * generate a random integer number from [1, max]
     */
    public int getRandom()
    {
        Random rn = new Random();
        int rand = rn.nextInt(max);
        return rand;
    }
    
    public void testRandom()
    {
        for (int i = 0; i <= 100; i++)
        {
            System.out.println(getRandom());
        }
    }
}
