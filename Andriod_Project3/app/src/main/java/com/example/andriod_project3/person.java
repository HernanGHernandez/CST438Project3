package com.example.andriod_project3;

public class person {
    String name;
    String password;
    public person(String name1, String password1)
    {
        name = name1;
        password = password1;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
