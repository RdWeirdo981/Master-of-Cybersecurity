import java.util.ArrayList;
/**
 * Write a description of class ObservationPoint here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class ObservationPoint
{
    private ArrayList<Koala> healthyKoalas; // [HK1, HK2, ..., HK n]
    private ArrayList<Koala> injuredKoalas; // [IK1, IK2, ...IK i]
    private ArrayList<Tree> trees; // [Tree1, Tree2, ..., Tree m]
    private double food;
    private int damages;
    private int deads;
    private int predators; 
    private int[] treeNumber;
    
    /**
     * Default Constructor for objects of class ObservationPoint
     */
    public ObservationPoint()
    {
        healthyKoalas = new ArrayList<Koala>();
        injuredKoalas = new ArrayList<Koala>();
        trees = new ArrayList<Tree>();
        food = 0.00;
        damages = 0;
        deads = 0;
        predators = 0;
        int[] treeNumber = {0, 0, 0, 0, 0};
    }
    
    /**
     * Parametered Constructor
     * 
     * @para: healthym injured, treeList, predator, food, tree, damageTree, death
     */
    public ObservationPoint(ArrayList<Koala> healthy, ArrayList<Koala> injured, ArrayList<Tree> treeList, 
                                                    int predator, double food, int[] tree, int damageTree, int death)
    {
        healthyKoalas = healthy;
        injuredKoalas = injured;
        trees = treeList;
        predators = predator;
        this.food = food;
        treeNumber = tree;
        damages = damageTree;
        deads = death;
    }
    
    /**
     * Method getKoalas
     * 
     * return an arraylist of healthy Koala class [HK1, HK2, ...]
     */
    public ArrayList<Koala> getHealthyKoalas()
    {
        return healthyKoalas;
    }
    
    /**
     * Method getInjuredKoalas
     * 
     * return an arraylist of injured Koala class [IK1, IK2 ...]
     */
    public ArrayList<Koala> getInjuredKoalas()
    {
        return injuredKoalas;
    }
    
    /**
     * Method getTrees
     * 
     * return an arraylist of Tree class [Tree1, Tree2, ...]
     */
    public ArrayList<Tree> getTrees()
    {
        return trees;
    }
    
    /**
     * Method getFood
     * 
     * return a double value of available food
     */
    public double getFood()
    {
        return food;
    }
    
    /**
     * Method getDamages
     * 
     * return a number of damages of tree
     */
    public int getDamages()
    {
        return damages;
    }
    
    /**
     * Method getDead
     * 
     * return a number of dead koalas
     */
    public int getDead()
    {
        return deads;
    }
    
    /**
     * Method getHealthyNo
     * 
     * get the number of healthy koalas
     */
    public int getHealthyNo()
    {
        return healthyKoalas.size();
    }
    
    /**
     * Method getInjuredNo
     * 
     * get the number of injured koalas
     */
    public int getInjuredNo()
    {
        return injuredKoalas.size();
    }
    
    /**
     * Method getPredators
     * 
     * return the number of predator
     */
    public int getPredators()
    {
        return predators;
    }
    
    /**
     * Method getTreeNumber
     * 
     * return an int[] of tree number
     */
    public int[] getTreeNumber()
    {
        return treeNumber;
    }
    
    /**
     * Method setHealthyKoalas
     * 
     * pass a koala list to healthyKoalas
     */
    public void setHealthyKoalas(ArrayList<Koala> koalas)
    {
        healthyKoalas = koalas;
    }
    
    /**
     * Method setInjuredKoalas
     * 
     * pass a koala list to injuredKoalas
     */
    public void setInjuredKoalas(ArrayList<Koala> koalas)
    {
        injuredKoalas = koalas;
    }
    
    /**
     * Method setDead
     * 
     * set dead koalas number
     */
    public void setDead(int dead)
    {
        deads = dead;
    }
    
    /**
     * Method setDamages
     * 
     * set the damages of tree
     */
    public void setDamages(boolean[] damageTree)
    {
        for (int i = 0; i < 5; i++)
        {
            if (damageTree[i])
            {
                damages++;
            }
        }
    }
    
    /**
     * Method addHealthyKoala
     * 
     * add a Koala to the healthy koalas
     */
    public void addHealthyKoala(int age)
    {
        Koala koala = new Koala(true, age);
        healthyKoalas.add(koala);
    }
    
    /**
     * Method addInjuredKoala
     * 
     * add a Koala to the injured koalas
     */
    public void addInjuredKoala(int age)
    {
        Koala koala = new Koala(false, age);
        injuredKoalas.add(koala);
    }
    
    /**
     * Method addTree
     * 
     * add a Tree to the trees
     */
    public void addTree(String type)
    {
        Tree tree = new Tree(type);
        trees.add(tree);
    }
    
    /** Method initialHealthyKoalas
     * 
     * assign age to healthy koalas
     */
    public void initialHealthyKoalas(int number, ArrayList<Integer> ageList)
    {
        for (int i = 0; i < number; i++)
        {
            int age = ageList.get(i);
            addHealthyKoala(age);
        }
    }
    
    /** Method initialInjuredKoalas
     * 
     * assign age to injured koalas
     */
    public void initialInjuredKoalas(int number, ArrayList<Integer> ageList)
    {
        for (int i = 0; i < number; i++)
        {
            int age = ageList.get(i);
            addInjuredKoala(age);
        }
    }
    
    /**
     * Method setTrees
     * 
     * set whole type of trees
     */
    public void setTrees()
    {
        int manna = treeNumber[0];
        int swamp = treeNumber[1];
        int blue = treeNumber[2];
        int redRiver = treeNumber[3];
        int wattle = treeNumber[4];
        for (int i = 0; i < manna; i++)
        {
            addTree("Manna Gum");
        }
        for (int i = 0; i < swamp; i++)
        {
            addTree("Swamp Gum");
        }
        for (int i = 0; i < blue; i++)
        {
            addTree("Blue Gum");
        }
        for (int i = 0; i < redRiver; i++)
        {
            addTree("River Red Gum");
        }
        for (int i = 0; i < wattle; i++)
        {
            addTree("Wattle");
        }
    }
    
    /** Method setPredators
     * 
     * set the predators number
     */
    public void setPredators(int number)
    {
        predators = number;
    }
    
    /**
     * Method setFood
     * 
     * set the whole food suply for this Observation Point
     */
    public void setFood()
    {
        food = treeNumber[0] * 1.00 + treeNumber[1] * 0.34 + treeNumber[2] * 0.90 + treeNumber[3] * 0.40;
    }
    
    /**
     * Method setTreeNumber
     * 
     * set the tree number after damage applied
     */
    public void setTreeNumber(int[] tree)
    {
        treeNumber = tree;
    }
    
    /**
     * Method printInfo
     * 
     * print the infomation of this observation
     */
    public void printInfo()
    {
        System.out.println("Injured Koalas: " + getInjuredNo());
        System.out.println("Healthy Koalas: " + getHealthyNo());
        System.out.println("Total food: " + food);
        System.out.println("Total shelter: " + treeNumber[4]);
        System.out.println("Total predators: " + predators);
        System.out.println("\n");
    }
    
    /**
     * Method moveInjured
     * 
     * move an injured Koala to the safe haven
     */
    public void moveInjured()
    {
        injuredKoalas.remove(0);
    }
    
    /**
     * Method moveHealthy
     * 
     * move a healthy Koala to the safe haven
     */
    public void moveHealthy()
    {
        healthyKoalas.remove(0);
    }
    
    /**
     * Method receiveKoala
     * 
     * add this oldest Koala in healthy list
     */
    public void receiveKoala(int age)
    {
        addHealthyKoala(age);
    }
    
    /**
     * Method relocateCondition
     * 
     * check relocation condition
     */
    public boolean relocateCondition()
    {
        int wholeKoalas = healthyKoalas.size() + injuredKoalas.size() + 1;
        int shelter = treeNumber[4];
        if (wholeKoalas <= food && wholeKoalas <= shelter && predators < 3)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
