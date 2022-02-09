package com.aws.sample.web.app.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    /**
     * 获取所有服务
     */
    @GetMapping("/hello")
    public String hello() {

        String res = "say hello";
        return res.toString();
    }

}
