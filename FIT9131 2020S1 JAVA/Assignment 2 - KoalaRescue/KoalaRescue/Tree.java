
/**
 * Tree class.
 *
 * @06-12-2020
 */
public class Tree
{
    // there is only one tree in a Tree class
    private String treeType; // Tree's type

    /**
     * Default Tree constructor
     */
    public Tree()
    {
        setTreeType("Empty");
    }
    
    /**
     * Parameterized constructor
     */
    public Tree(String type)
    {
        boolean validCheck = setTreeType(type);
        if (!validCheck)
        {
            setTreeType("Empty");
        }
    }

    /**
     * Method getTreeType
     * 
     * return the String of type of the tree
     */
    public String getTreeType()
    {
        return treeType;
    }
    
    /**
     * Method setTreeType
     * 
     * set the type of the tree and returen a boolean number to see if it works
     */
    public boolean setTreeType(String type)
    {
        if (type.equals("Manna Gum") || type.equals("Swamp Gum") || type.equals("Blue Gum") || type.equals("River Red Gum")
                                                                          || type.equals("Wattle") || type.equals("Empty"))
        {
            treeType = type;
            return true;
        }
        else
        {
            return false;
        }
    }
}
