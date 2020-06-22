import React, { Component } from "react";
import { render } from "react-dom";
import Nav from './Nav'

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
      <div className="container mx-auto">
      <Nav/>
      <div class="flex flex-col">
        <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
          <div class="align-middle inline-block min-w-full shadow overflow-hidden sm:rounded-lg border-b border-gray-200">
            <table class="min-w-full">
              <thead>
                <tr>
                  <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Phrase
                  </th>
                  <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Count
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white">
                {this.state.data.map((phraselist) => {
                  return (
                    <tr key={phraselist.id}>
                      <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                        <div class="flex items-center">
                          <div class="ml-4">
                            <div class="text-sm leading-5 text-gray-900">
                              {phraselist.phrase}
                            </div>
                          </div>
                        </div>
                      </td>
                      <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                        <div class="text-sm leading-5 text-gray-900">
                          {phraselist.count}
                        </div>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
