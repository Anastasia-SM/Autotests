Feature: test-case 1.2

Scenario: Сheck that task is added to a new category

  Given website "qa-assignment.oblakogroup.ru/board/:anastasia_sakova"
  When push button with a plus
  And choose category 'Создать новый список'
  And type category name 'День рождения'
  And type task name 'Испечь торт'
  And push OK button
  Then 'День рождения' includes a task 'Испечь торт'