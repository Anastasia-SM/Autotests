# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import os

#Откроем страницу с платформой для создания категоризированных to-do листов
@given('website "{url}"')
def step(context, url):
    context.browser = webdriver.Chrome()
    #context.browser.maximize_window()
    context.browser.get("http://qa-assignment.oblakogroup.ru/board/:anastasia_sakova")

#Нажмем на кнопку со знаком "+" чтобы добавить новую задачу
@when("push button with a plus")
def step(context):
    context.browser.find_element_by_id("add_new_todo").click()
    
#Выберем категорию. Категория передается в качестве аргумента 
@when("choose category '{text}'")
def step(context, text):
    select = Select(context.browser.find_element_by_id("select_category"))
    select.select_by_visible_text(text)  
 
#Напишем заголовок категории. Заголовок передается в качестве аргумента 
@when("type category name '{cat}'")
def step(context, cat):    
    context.browser.find_element_by_xpath("//input[@id='project_title']").clear()
    context.browser.find_element_by_xpath("//input[@id='project_title']").send_keys(cat)
 
#Напишем название задачи. Название передается в качестве аргумента    
@when("type task name '{text}'")
def step(context, text):    
    context.browser.find_element_by_xpath("//input[@id='project_text']").clear()
    context.browser.find_element_by_xpath("//input[@id='project_text']").send_keys(text)
 
#Нажимаем кнопку "ОК"
@when("push OK button")
def step(context):
    context.browser.find_element_by_xpath("//a[@id='submit_add_todo']").click()
    
#Проверим, что на странице в нужной категории появилась новая задача. Категория и задача передаются в качестве аргументов
@then("'{cat}' includes a task '{text}'")
def step(context, cat, text):
    context.browser.find_element_by_xpath("//h2[contains(text(),cat)]").find_element_by_xpath("//label[contains(text(),text)]")
    context.browser.quit()  
