Feature: test-case 1.1

Scenario: Сheck that task is added

  Given website "qa-assignment.oblakogroup.ru/board/:anastasia_sakova"
  When push button with a plus
  And choose category 'Прочее'
  And type task name 'Попить кофе'
  And push OK button
  Then 'Прочее' includes a task 'Попить кофе'
 