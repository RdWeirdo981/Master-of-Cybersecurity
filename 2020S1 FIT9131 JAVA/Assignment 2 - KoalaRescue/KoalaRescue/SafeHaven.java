import java.util.ArrayList;
/**
 * Write a description of class SafeHaven here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class SafeHaven
{
    // instance variables - replace the example below with your own
    private ArrayList<Koala> healthyKoalas; // Healthy Koala in Safe Haven. [Koala1, ..., Koala i]
    private ArrayList<Koala> injuredKoalas;
    private int relocates; // the number of relocated Koalas

    /**
     * Constructor for objects of class SafeHaven
     */
    public SafeHaven()
    {
        healthyKoalas = new ArrayList<Koala>();
        injuredKoalas = new ArrayList<Koala>();
        relocates = 0;
    }
    
    /**
     * parametered constructor
     * 
     */
    public SafeHaven(ArrayList<Koala> healthy, ArrayList<Koala> injured, int relocatedNumber)
    {
        healthyKoalas = healthy;
        injuredKoalas = injured;
        relocates = relocatedNumber;
    }
    
    /**
     * Method getHealthyKoala
     * 
     * return a list of healthy Koala in safe haven
     */
    public ArrayList<Koala> getHealthyKoalas()
    {
        return healthyKoalas;
    }
    
    /**
     * Method getInjuredKoala
     * 
     * return a list of injured Koala in safe haven
     */
    public ArrayList<Koala> getInjuredKoalas()
    {
        return injuredKoalas;
    }
    
    /**
     * Method getRelocates
     * 
     * return an integer number of relocated Koala
     */
    public int getRelocates()
    {
        return relocates;
    }
    
    /**
     * Method addHealthyKoala
     * 
     * add a Koala to the koalas
     */
    public void addHealthyKoala(int age)
    {
        Koala koala = new Koala(true, age);
        healthyKoalas.add(koala);
    }
    
    /**
     * Method addInjuredKoala
     * 
     * add a Koala to the koalas
     */
    public void addInjuredKoala(int age)
    {
        Koala koala = new Koala(false, age);
        injuredKoalas.add(koala);
    }
    
    /**
     * Method getOldest
     * 
     * get the oldest index of healthy Koalas
     */
    public int getOldest()
    {
        if (healthyKoalas.size() > 0)
        {
            int oldest = 0;
            for (int i = 0; i < healthyKoalas.size()-1; i++)
            {
                if (healthyKoalas.get(oldest).getAge() < healthyKoalas.get(i+1).getAge())
                {
                    oldest = i+1;
                }
            }
            return oldest;
        }
        else
        {
            return 0;
        }
    }
    
    /**
     * Method existHealthy
     * 
     * check if existHealthy
     */
    public boolean existHealthy()
    {
        boolean validCheck = true;
        if (healthyKoalas.size() <= 0)
        {
            validCheck = false;
        }
        return validCheck;
    }
    
    /**
     * Method relocateKoala
     * 
     * relocate the oldest Koala from the Save Haven to observation point
     */
    public void relocateKoala()
    {
        boolean validCheck = existHealthy();
        if (validCheck = true)
        {
            int oldest = getOldest();
            healthyKoalas.remove(oldest);
            relocates++;
        }
    }
    
    /**
     * Method receiveInjured
     * 
     * receive an injured Koala
     */
    public void receiveInjured(int age)
    {
        addInjuredKoala(age);
    }
    
    /**
     * Method receiveInjured
     * 
     * receive an injured Koala
     */
    public void receiveHealthy(int age)
    {
        addHealthyKoala(age);
    }
}
