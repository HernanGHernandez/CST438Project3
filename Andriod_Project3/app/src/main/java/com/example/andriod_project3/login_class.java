package com.example.andriod_project3;

public class login_class {
    String name;
    String password;

    public login_class(String name1, String password2) {
        name = name1;
        password = password2;
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
