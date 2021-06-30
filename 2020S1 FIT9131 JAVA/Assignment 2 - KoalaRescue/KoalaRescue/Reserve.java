import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
/**
 * Write a description of class Reserve here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Reserve
{
    private ArrayList<ObservationPoint> pointList; // [Point1, Point2, ..., Point10]
    private int[][] treeNumber;
    private RandomNumber random;
    private SafeHaven safeHaven;
    
    /**
     * Constructor for objects of class Reserve
     */
    public Reserve()
    {
        // initialise instance variables
        random = new RandomNumber();
        safeHaven = new SafeHaven();
        pointList = new ArrayList<ObservationPoint>();
        treeNumber = new int[10][5]; // 0 - 9 * 0 - 4
    }
    
    /**
     * parametered constructor
     * 
     */
    public Reserve(RandomNumber randomNumber, SafeHaven haven, ArrayList<ObservationPoint> point, int[][] tree)
    {
        random = randomNumber;
        safeHaven = haven;
        pointList = point;
        treeNumber = tree;
    }
    
    /**
     * Method getSafeHaven
     * 
     * return SafeHaven 
     */
    public SafeHaven getSafeHaven()
    {
        return safeHaven;
    }
    
    /**
     * Method getPointList
     * 
     * return a list containing ObservationPoint class
     */
    public ArrayList<ObservationPoint> getPointList()
    {
        return pointList;
    }
    
    /**
     * Method addPoint
     * 
     * add observation point into Reserve
     */
    public void addPoint(ObservationPoint point)
    {
        pointList.add(point);
    }
    
    /**
     * Method assignPredators
     * 
     * pass random predator number to an Observation point
     */
    public void assignPredators(ObservationPoint point)
    {
        random.setMax(5);
        int predators = random.getRandom();
        point.setPredators(predators);
    }
    
    /**
     * Method assignHealthyKoalas
     * 
     * pass random Koalas: healthy K, injured K, age list to an observation point
     */
    public void assignHealthyKoalas(ObservationPoint point)
    {
        random.setMax(10);
        int healthy = random.getRandom();
        ArrayList<Integer> ageList = new ArrayList<Integer>();
        random.setMax(18);
        for (int i = 0; i < healthy; i++)
        {
            int age = random.getRandom() + 1; // 0 to 17 becomes to  1 to 18
            ageList.add(age);
        }
        point.initialHealthyKoalas(healthy, ageList);
    }
    
    /**
     * Method assignInjuredKoalas
     * 
     * pass random Koalas: healthy K, injured K, age list to an observation point
     */
    public void assignInjuredKoalas(ObservationPoint point)
    {
        random.setMax(3);
        int injured = random.getRandom();
        ArrayList<Integer> ageList = new ArrayList<Integer>();
        random.setMax(18);
        for (int i = 0; i < injured; i++)
        {
            int age = random.getRandom() + 1; // 0 to 17 becomes to  1 to 18
            ageList.add(age);
        }
        point.initialInjuredKoalas(injured, ageList);
    }
    
    /**
     * Method readTree
     * 
     * read the tree file and return an int[][] array to 10 observation point
     */
    public void readTree()
    {
        String fileName = "trees.txt";
        try
        {
            FileReader file = new FileReader(fileName);
            Scanner parser = new Scanner(file);
            try
            {
                int index = 0;
                while (parser.hasNextLine())
                {
                    int[] treeList = {0, 0, 0, 0, 0};
                    String line = parser.nextLine();
                    if (line.length() == 0)
                    {
                        continue;
                    }
                    else
                    {
                        String[] trees = line.split(",");
                        for (int n = 0; n < 5; n++)
                        {
                            treeNumber[index][n] = Integer.parseInt(trees[n]);
                        }
                        index++;
                    }
                }
                System.out.println("\n");
                System.out.println("'trees.txt' read finished.");
            }
            catch (Exception exception)
            {
                System.out.println(exception);
            }
            finally
            {
                file.close();
                parser.close();
                System.out.println("File is closed.");
                System.out.println("\n");
            }
        }
        catch (FileNotFoundException exception)
        {
            System.out.println("\n");
            System.out.println("Error: " + fileName + " cannot be found!");
            System.out.println("Please place the file in the right path, and restart the rescue.");
        }
        catch (IOException exception)
        {
            System.out.println("\n");
            System.out.println("Error: " + fileName + " cannot be closed!");
        }
    }
    
    /**
     * Method assignTreeNumber
     * 
     * assign tree numbers to an observation
     */
    public void assignTreeNumber(int index, ObservationPoint point)
    {
        applyDamage(treeNumber[index], point);
        point.setTreeNumber(treeNumber[index]);
    }
    
    /**
     * Method getDamage
     * 
     * assign damge list for one observation point
     */
    public boolean[] getDamage()
    {
        boolean[] damageList = {false, false, false, false, false};
        random.setMax(20); // 0 to 19
        for (int n = 0; n < 5; n++)
        {
            int probability = random.getRandom();
            if (probability == 0) // 0 = damage happens, 1 - 19 = damage not happen
            {
                damageList[n] = true;
            }
        }
        return damageList;
    }
    
    /**
     * Method applyDamage
     * 
     * apply Damage to tree list
     */
    public void applyDamage(int[] line, ObservationPoint point)
    {
        boolean[] damage = getDamage();
        for (int n = 0; n < 5; n++)
        {
            if (damage[n] == true && line[n] > 0)
            {
                line[n] -= 1;
            }
            else if (line[n] <= 0)
            {
                damage[n] = false; // no tree no damage
            }
        }
        point.setDamages(damage);
    }
    
    /**
     * Method initialPoint
     * 
     * initializes pointList
     */
    public void initialPoint()
    {
        readTree();
        for (int n = 0; n < 10; n++)
        {
            ObservationPoint point = new ObservationPoint();
            assignHealthyKoalas(point);
            assignInjuredKoalas(point);
            assignPredators(point);
            assignTreeNumber(n, point);
            point.setTrees();
            point.setFood();
            addPoint(point);
        }
    }
    
    /**
     * Method printInfo
     * 
     * print observation point info
     */
    public void printInfo(int index)
    {
        System.out.println("\n");
        System.out.println("Observation point " + (index+1));
        pointList.get(index).printInfo();
    }
    
    /**
     * Method moveInjured
     * 
     * movde an injured koala to the safe haven
     */
    public void moveInjured(int index)
    {
        int age = pointList.get(index).getInjuredKoalas().get(0).getAge(); // get this koala's age
        pointList.get(index).moveInjured();
        safeHaven.receiveInjured(age);
    }
    
    /**
     * Method validInjured
     * 
     * check if move injured valid
     */
    public boolean validInjured(int index)
    {
        if (pointList.get(index).getInjuredNo() <= 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    
    /**
     * Method moveHealthy
     * 
     * movde an injured koala to the safe haven
     */
    public void moveHealthy(int index)
    {
        int age = pointList.get(index).getHealthyKoalas().get(0).getAge(); // get this koala's age
        pointList.get(index).moveHealthy();
        safeHaven.receiveHealthy(age);
    }
    
    /**
     * Method validHealthy
     * 
     * check if move healthy valid
     */
    public boolean validHealthy(int index)
    {
        if (pointList.get(index).getHealthyNo() <= 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    
    /**
     * Method relocateKoala
     * 
     * relocate a Koala form safe haven to observation point
     */
    public void relocateKoala(int index)
    {
        int number = safeHaven.getOldest();
        int age = safeHaven.getHealthyKoalas().get(number).getAge();
        safeHaven.relocateKoala();
        pointList.get(index).receiveKoala(age);
    }
    
    /**
     * Method relocateCheck
     * 
     * check if relocate can happen
     */
    public boolean validRelocate(int index)
    {
        boolean validHaven = safeHaven.existHealthy();
        boolean validPoint = pointList.get(index).relocateCondition();
        if (validHaven && validPoint)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    
    /**
     * Method assessDead
     * 
     * assess the number of dead koalas in specific observation point
     */
    public void assessDead(int index)
    {
        ObservationPoint point = pointList.get(index);
        int injureds = point.getInjuredKoalas().size(); // assess Injured Koalas
        int shortageFood = point.getHealthyKoalas().size() - (int)point.getFood(); // assess food shortage
        int foodDeath = 0;
        random.setMax(5);
        for (int n = 0; n < shortageFood; n++)  // if shortageFood <=0, this loop will not happen
        {
            int probabilityFood = random.getRandom();
            if (probabilityFood >= 0 && probabilityFood <= 3)
            {
                foodDeath++;
                point.getHealthyKoalas().remove(n);
                pointList.get(index).setHealthyKoalas(point.getHealthyKoalas());
                shortageFood = point.getHealthyKoalas().size() - (int)point.getFood();
            }
        }
        int[] trees = point.getTreeNumber(); // assess shelter shortage
        int shortageShelter = point.getHealthyKoalas().size() - trees[4];
        int shelterDeath = 0;
        for (int m = 0; m < shortageShelter; m++)
        {
            int probabilityShelter = random.getRandom();
            if (probabilityShelter == 1)
            {
                shelterDeath++;
                point.getHealthyKoalas().remove(m);
                pointList.get(index).setHealthyKoalas(point.getHealthyKoalas());
                shortageShelter = point.getHealthyKoalas().size() - trees[4];
            }
        }
        int predators = point.getPredators();
        int predatorDeath = 0;
        if (predators > 3 && point.getHealthyKoalas().size() > 0)
        {
            random.setMax(2);
            int probabilityPredator = random.getRandom();
            if (probabilityPredator == 1)
            {
                predatorDeath++;
                point.getHealthyKoalas().remove(0);
                pointList.get(index).setHealthyKoalas(point.getHealthyKoalas());
            }
        }
        int totalDeath = injureds + foodDeath + shelterDeath + predatorDeath;
        pointList.get(index).setDead(totalDeath);
    }
    
    /**
     * Method getTotalDeads()
     * 
     */
    public int getTotalDeads()
    {
        int deads = 0;
        for (int n = 0; n < 10; n++)
        {
            deads += pointList.get(n).getDead();
        }
        return deads;
    }
    
    /**
     * Method getOnePointDeads()
     * 
     */
    public int getOnePointDeads(int index)
    {
        return pointList.get(index).getDead();
    }
    
    /**
     * Method getDamages
     * 
     * get the whole damage number of tree
     */
    public int getTotalDamage()
    {
        int damages = 0;
        for (int n = 0; n < 10; n++)
        {
            damages += pointList.get(n).getDamages();
        }
        return damages;
    }
    
    /**
     * Method getTotalKoalas
     */
    public int getTotalHealthy()
    {
        int healthyKoalas = 0;
        for (int n = 0; n < 10; n++)
        {
            healthyKoalas += pointList.get(n).getHealthyKoalas().size();
        }
        healthyKoalas += safeHaven.getHealthyKoalas().size();
        return healthyKoalas;
    }
    
    /**
     * Method getTotalKoalas
     */
    public int getTotalInjured()
    {
        int injuredKoalas = 0;
        for (int n = 0; n < 10; n++)
        {
            injuredKoalas += pointList.get(n).getInjuredKoalas().size();
        }
        return injuredKoalas;
    }
    
    /**
     * Method getRelocates
     * 
     */
    public int getRelocates()
    {
        return safeHaven.getRelocates();
    }
    
    /**
     * Method writeUpdate
     */
    public void writeUpdate()
    {
        String fileName = "updatedTrees.txt";
        try
        {
            PrintWriter writer = new PrintWriter(fileName);
            try
            {
                for (int index = 0; index < 10; index++)
                {
                    String line = "";
                    for (int n = 0; n < 4 ; n++)
                    {
                        line += treeNumber[index][n] + ",";
                    }
                    line += treeNumber[index][4];
                    writer.append(line + "\n");
                }
            }
            catch (Exception exception)
            {
                System.out.println(exception);
            }
            finally
            {
                writer.close();
            }
        }
        catch (IOException exception)
        {
            System.out.println("\n");
            System.out.println("Error: " + fileName + " cannot be opened!");
        }
    }
}
