class testComponent extends React.Component{
  render() {
    return (<h2>Greetings, from Real Python!</h2>);
  }
}

ReactDOM.render(
  React.createElement(testComponent, null),
  document.getElementById('content')
);