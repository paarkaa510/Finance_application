// static/js/charts.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Custom script loaded');

    const expensesData = JSON.parse(document.getElementById('expensesData').textContent);
    const expensesLabels = expensesData.map(expense => expense.category);
    const expensesAmounts = expensesData.map(expense => expense.total);

    const ctxPie = document.getElementById('expensesPieChart').getContext('2d');
    if (window.expensesPieChart && typeof window.expensesPieChart.destroy === 'function') {
        window.expensesPieChart.destroy();
    }
    window.expensesPieChart = new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: expensesLabels,
            datasets: [{
                data: expensesAmounts,
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']
            }]
        }
    });
    
    
});


