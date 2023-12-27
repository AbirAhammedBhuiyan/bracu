#ifndef TREE_NODE_H
#define TREE_NODE_H

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>


static int indent = 0;
static int activateIndent = 0;
static int space = 0;
static std::vector<std::string> scs = {"+", "*", "-", "=", "||", "&&", "<", "%"}; // space char space
static std::vector<std::string> nsc = {"(", ")", "[", "]"}; // no space char

class TreeNode {
private:
    std::string type;
    std::string value;
    std::vector<TreeNode*> children;

public:
    TreeNode(const std::string& type, const std::string& value = "") 
        : type(type), value(value) {}

    static TreeNode* createNonTerminalNode(const std::string& type) {
        return new TreeNode(type);
    }

    static TreeNode* createTerminalNode(const std::string& type, const std::string& value = "") {
        return new TreeNode(type, value);
    }

    void addChild(TreeNode* child) {
        children.push_back(child);
    }

    const std::string& getType() const {
        return type;
    }

    const std::string& getValue() const {
        return value;
    }

    const std::vector<TreeNode*>& getChildren() const {
        return children;
    }

    int getNumChildren() const {
        return children.size();
    }

    void postOrderTraversal(std::ofstream& outFile) {
        for (auto child : children) {
            child->postOrderTraversal(outFile);
        }

        if (!value.empty()) {
            if (value.compare("{") == 0) {
                outFile << " " << value << std::endl;
                indent++;
                activateIndent = 1;
            } else if (value.compare("}") == 0) {
                outFile << value << std::endl<<std::endl;
                indent--;
                activateIndent = 1;
                space = 0;
            } else if (value.compare(";") == 0) {
                outFile << value << std::endl;  
                activateIndent = 1;
                space = 0;
            } else if (std::find(nsc.begin(), nsc.end(), value) != nsc.end()) {
                outFile << value;  
                space = 0;
            } else if (std::find(scs.begin(), scs.end(), value) != scs.end()) {
                outFile << " " << value << " ";  
                space = 0;
            } else if (value.compare(",") == 0) {
                outFile << value<< " ";  
                space = 0;
            } else {
                if (activateIndent) {
                    for (int i=0; i<indent*4; i++) {
                        outFile << " ";
                    }
                    activateIndent = 0;
                }

                if (space) {
                    outFile << " ";
                    space = 0;
                } else {
                    space = 1;
                }
                outFile << value;
            }
        }
    }

    ~TreeNode() {
        for (auto child : children) {
            delete child;
        }
    }
};

#endif  // TREE_NODE_H
