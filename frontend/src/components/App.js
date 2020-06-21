import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/phraselist")
      .then((response) => {
        console.log(response);
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        this.setState(() => {
          return {
            data: data.results,
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <table className="table-auto">
        <thead>
          <tr>
            <th className="px-4 py-2">Phrase</th>
            <th className="px-4 py-2">Count</th>
          </tr>
        </thead>
        <tbody>
          {this.state.data.map((phraselist) => {
            return (
              <tr className="bg-gray-100" key={phraselist.id}>
                <td class="border px-4 py-2">{phraselist.phrase}</td>
                <td class="border px-4 py-2">{phraselist.count}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
