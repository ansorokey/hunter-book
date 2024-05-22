import './index.css';
import MonsterPage from './components/MonsterPage/index.jsx';
import MonsterScrollBar from './components/MonsterScrollBar/index';
import SearchBar from './components/SearchBar/index';

function App() {
  return (
    <div id="app-wrapper">
      <h1>Hello World from App.tsx</h1>
      <SearchBar/>
      <MonsterPage/>
      <MonsterScrollBar/>
    </div>
  );
}

export default App;
