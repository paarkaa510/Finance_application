document.addEventListener('DOMContentLoaded', function() {
    // Data for Pie Chart
    const expensesData = JSON.parse(document.getElementById('expensesData').textContent);
    const expensesLabels = expensesData.map(expense => expense.category);
    const expensesAmounts = expensesData.map(expense => expense.total);


    const ctxPie = document.getElementById('expensesPieChart').getContext('2d');
    new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: expensesLabels,
            datasets: [{
                data: expensesAmounts,
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']
            }]
        }
    });







})